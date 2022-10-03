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
  { Pos: 1 ,Nombre: "Eduardo",   Juegos: 333, Ganados: 203, Perdidos: 130,  Dif: '-', Porcentaje: 610, diasPerfectos: 8},
  { Pos: 2 ,Nombre: "Steven",    Juegos: 333, Ganados: 203, Perdidos: 130,  Dif: '-', Porcentaje: 610, diasPerfectos: 10},
  { Pos: 3 ,Nombre: "CarlosJ",   Juegos: 333, Ganados: 198, Perdidos: 135,  Dif:  5,  Porcentaje: 595, diasPerfectos: 91},
  { Pos: 4 ,Nombre: "Kleydi",    Juegos: 333, Ganados: 193, Perdidos: 140,  Dif:  10, Porcentaje: 580, diasPerfectos: 9},
  { Pos: 5 ,Nombre: "Daniel",    Juegos: 333, Ganados: 187, Perdidos: 146,  Dif:  16, Porcentaje: 560, diasPerfectos: 1},
  { Pos: 6 ,Nombre: "Erycherd",  Juegos: 333, Ganados: 185, Perdidos: 148,  Dif:  18, Porcentaje: 555, diasPerfectos: 5},
  { Pos: 7 ,Nombre: "Christian", Juegos: 333, Ganados: 183, Perdidos: 151,  Dif:  20, Porcentaje: 550, diasPerfectos: 17},
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