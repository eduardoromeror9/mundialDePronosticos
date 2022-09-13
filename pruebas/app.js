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
  { Pos: 1 ,Nombre: "Eduardo",   Juegos: 291, Ganados: 178, Perdidos: 113,  Dif: '-',  Porcentaje: 610, diasPerfectos: 8},
  { Pos: 2 ,Nombre: "Steven",    Juegos: 291, Ganados: 174, Perdidos: 117,  Dif:  4,   Porcentaje: 595, diasPerfectos: 10},
  { Pos: 3 ,Nombre: "CarlosJ",   Juegos: 291, Ganados: 172, Perdidos: 119,  Dif:  6,   Porcentaje: 590, diasPerfectos: 9165458},
  { Pos: 4 ,Nombre: "Kleydi",    Juegos: 291, Ganados: 169, Perdidos: 122,  Dif:  9,   Porcentaje: 580, diasPerfectos: 9},
  { Pos: 5 ,Nombre: "Daniel",    Juegos: 291, Ganados: 163, Perdidos: 128,  Dif:  15,  Porcentaje: 560, diasPerfectos: 1},
  { Pos: 6 ,Nombre: "Christian", Juegos: 291, Ganados: 160, Perdidos: 131,  Dif:  18,  Porcentaje: 550, diasPerfectos: 17},
  { Pos: 7 ,Nombre: "Erycherd",  Juegos: 291, Ganados: 158, Perdidos: 133,  Dif:  20,  Porcentaje: 540, diasPerfectos: 5},
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
                         🧊      Huele a Back To Back      🧊
                         🧊      Huele a Back To Back      🧊  
                         🧊      Huele a Back To Back      🧊  
                         🧊                                🧊
                         🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊 \n`

console.log(info.blue.bold);

table(test);