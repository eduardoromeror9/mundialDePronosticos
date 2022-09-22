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
  { Pos: 1 ,Nombre: "Eduardo",   Juegos: 306, Ganados: 186, Perdidos: 120,  Dif: '-', Porcentaje: 610, diasPerfectos: 8},
  { Pos: 2 ,Nombre: "Steven",    Juegos: 306, Ganados: 185, Perdidos: 121,  Dif:  1,  Porcentaje: 605, diasPerfectos: 10},
  { Pos: 3 ,Nombre: "CarlosJ",   Juegos: 306, Ganados: 182, Perdidos: 124,  Dif:  4,  Porcentaje: 595, diasPerfectos: 9165458},
  { Pos: 4 ,Nombre: "Kleydi",    Juegos: 306, Ganados: 178, Perdidos: 128,  Dif:  8,  Porcentaje: 580, diasPerfectos: 9},
  { Pos: 5 ,Nombre: "Daniel",    Juegos: 306, Ganados: 173, Perdidos: 133,  Dif:  13, Porcentaje: 565, diasPerfectos: 1},
  { Pos: 6 ,Nombre: "Erycherd",  Juegos: 306, Ganados: 168, Perdidos: 138,  Dif:  18, Porcentaje: 550, diasPerfectos: 5},
  { Pos: 7 ,Nombre: "Christian", Juegos: 306, Ganados: 167, Perdidos: 139,  Dif:  19, Porcentaje: 545, diasPerfectos: 17},
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
                         🧊      NO Huele a Back To Back   🧊
                         🧊      NO Huele a Back To Back   🧊  
                         🧊      NO Huele a Back To Back   🧊  
                         🧊                                🧊
                         🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊 \n`

console.log(info.blue.bold);

table(test);