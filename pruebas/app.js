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
  { Pos: 1 ,Nombre: "Eduardo",   Juegos: 322, Ganados: 196, Perdidos: 126,  Dif: '-', Porcentaje: 610, diasPerfectos: 8},
  { Pos: 2 ,Nombre: "Steven",    Juegos: 322, Ganados: 194, Perdidos: 128,  Dif:  2,  Porcentaje: 600, diasPerfectos: 10},
  { Pos: 3 ,Nombre: "CarlosJ",   Juegos: 322, Ganados: 192, Perdidos: 130,  Dif:  4,  Porcentaje: 595, diasPerfectos: 91},
  { Pos: 4 ,Nombre: "Kleydi",    Juegos: 322, Ganados: 186, Perdidos: 136,  Dif:  10, Porcentaje: 575, diasPerfectos: 9},
  { Pos: 5 ,Nombre: "Daniel",    Juegos: 322, Ganados: 180, Perdidos: 142,  Dif:  16, Porcentaje: 560, diasPerfectos: 1},
  { Pos: 6 ,Nombre: "Erycherd",  Juegos: 322, Ganados: 178, Perdidos: 144,  Dif:  18, Porcentaje: 550, diasPerfectos: 5},
  { Pos: 7 ,Nombre: "Christian", Juegos: 322, Ganados: 178, Perdidos: 144,  Dif:  18, Porcentaje: 550, diasPerfectos: 17},
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
                         🧊   CUIDADO con el Back To Back  🧊
                         🧊   CUIDADO con el Back To Back  🧊  
                         🧊   CUIDADO con el Back To Back  🧊  
                         🧊                                🧊
                         🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊 \n`

console.log(info.blue.bold);

table(test);