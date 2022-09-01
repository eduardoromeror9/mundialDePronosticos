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
  { Pos: 1 ,Nombre: "Eduardo",   Juegos: 265, Ganados: 161, Perdidos: 104,  Dif: '-',  Porcentaje: 610, diasPerfectos: 5},
  { Pos: 2 ,Nombre: "Steven",    Juegos: 265, Ganados: 158, Perdidos: 107,  Dif:  3,   Porcentaje: 595, diasPerfectos: 4},
  { Pos: 3 ,Nombre: "Kleydi",    Juegos: 265, Ganados: 156, Perdidos: 109,  Dif:  5,   Porcentaje: 585, diasPerfectos: 3},
  { Pos: 4 ,Nombre: "CarlosJ",   Juegos: 265, Ganados: 156, Perdidos: 109,  Dif:  5,   Porcentaje: 585, diasPerfectos: 98},
  { Pos: 5 ,Nombre: "Daniel",    Juegos: 265, Ganados: 149, Perdidos: 116,  Dif:  12,  Porcentaje: 560, diasPerfectos: 2},
  { Pos: 6 ,Nombre: "Christian", Juegos: 265, Ganados: 142, Perdidos: 123,  Dif:  19,  Porcentaje: 535, diasPerfectos: 1},
  { Pos: 7 ,Nombre: "Erycherd",  Juegos: 264, Ganados: 139, Perdidos: 125,  Dif:  22,  Porcentaje: 525, diasPerfectos: 2}
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
                         🧊   CarlosJ QUE PRENDA SU VELA   🧊
                         🧊   CarlosJ QUE PRENDA SU VELA   🧊  
                         🧊   CarlosJ QUE PRENDA SU VELA   🧊  
                         🧊                                🧊
                         🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊 \n`

console.log(info.blue.bold);

table(test);