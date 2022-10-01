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
  { Pos: 1 ,Nombre: "Eduardo",   Juegos: 328, Ganados: 200, Perdidos: 128,  Dif: '-', Porcentaje: 610, diasPerfectos: 8},
  { Pos: 2 ,Nombre: "Steven",    Juegos: 328, Ganados: 200, Perdidos: 128,  Dif: '-', Porcentaje: 610, diasPerfectos: 10},
  { Pos: 3 ,Nombre: "CarlosJ",   Juegos: 328, Ganados: 196, Perdidos: 132,  Dif:  4,  Porcentaje: 595, diasPerfectos: 91},
  { Pos: 4 ,Nombre: "Kleydi",    Juegos: 328, Ganados: 190, Perdidos: 138,  Dif:  10, Porcentaje: 580, diasPerfectos: 9},
  { Pos: 5 ,Nombre: "Daniel",    Juegos: 328, Ganados: 184, Perdidos: 144,  Dif:  16, Porcentaje: 560, diasPerfectos: 1},
  { Pos: 6 ,Nombre: "Christian", Juegos: 328, Ganados: 182, Perdidos: 146,  Dif:  18, Porcentaje: 555, diasPerfectos: 17},
  { Pos: 7 ,Nombre: "Erycherd",  Juegos: 328, Ganados: 181, Perdidos: 147,  Dif:  19, Porcentaje: 550, diasPerfectos: 5},
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