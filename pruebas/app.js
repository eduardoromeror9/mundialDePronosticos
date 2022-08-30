const { Console } = require('console');
const { Transform } = require('stream');
require('colors');


function table(input) {
  // @see https://stackoverflow.com/a/67859384
  const ts = new Transform({ transform(chunk, enc, cb) { cb(null, chunk) } })
  const logger = new Console({ stdout: ts })
  logger.table(input)
  const table = (ts.read() || '').toString()
  let result = ''; 
  for (let row of table.split(/[\r\n]+/)) {
    let r = row.replace(/[^┬]*┬/, '┌');
    r = r.replace(/^├─*┼/, '├');
    r = r.replace(/│[^│]*/, '');
    r = r.replace(/^└─*┴/, '└');
    r = r.replace(/'/g, ' ');
    result += `${r}\n`; 
  }
  console.log(result.red.bold);
}

const test = [
  { Pos: 1 ,Nombre: "Eduardo",   Juegos: 262, Ganados: 158, Perdidos: 104,  Dif: '-',  Porcentaje: 605, diasPerfectos: 5},
  { Pos: 2 ,Nombre: "Steven",    Juegos: 262, Ganados: 155, Perdidos: 107,  Dif:  3,   Porcentaje: 590, diasPerfectos: 4},
  { Pos: 3 ,Nombre: "CarlosJ",   Juegos: 262, Ganados: 154, Perdidos: 108,  Dif:  4,   Porcentaje: 585, diasPerfectos: 98},
  { Pos: 4 ,Nombre: "Kleydi",    Juegos: 262, Ganados: 153, Perdidos: 109,  Dif:  5,   Porcentaje: 580, diasPerfectos: 3},
  { Pos: 5 ,Nombre: "Daniel",    Juegos: 262, Ganados: 146, Perdidos: 116,  Dif:  12,  Porcentaje: 560, diasPerfectos: 2},
  { Pos: 6 ,Nombre: "Christian", Juegos: 262, Ganados: 140, Perdidos: 122,  Dif:  18,  Porcentaje: 535, diasPerfectos: 1},
  { Pos: 7 ,Nombre: "Erycherd",  Juegos: 262, Ganados: 138, Perdidos: 124,  Dif:  20,  Porcentaje: 525, diasPerfectos: 2}
];

let legend = 
  `\n        
                         🔥🔥 INFORMACION IMPORTANTE 🔥🔥
                              Don Eduardo Romero,
                              mejor conocido como
                              el KING de los PRONOSTICOS
                              ES EL VIGENTE CAMPEON
                                     HASTA QUE
                              SE DEMUESTRE LO CONTRARIO
  `
  console.log(legend.yellow.bold);

let info =`
                         🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊
                         🧊                                🧊
                         🧊      CarlosJ a la NEVERA       🧊
                         🧊      Steven a la NEVERA        🧊  
                         🧊      Kleydi a la NEVERA        🧊  
                         🧊                                🧊
                         🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊 \n`

console.log(info.blue.bold);

table(test);