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
  { Pos: 1 ,Nombre: "Eduardo",   Juegos: 303, Ganados: 186, Perdidos: 117,  Dif: '-', Porcentaje: 615, diasPerfectos: 8},
  { Pos: 2 ,Nombre: "Steven",    Juegos: 303, Ganados: 184, Perdidos: 119,  Dif:  2,  Porcentaje: 610, diasPerfectos: 10},
  { Pos: 3 ,Nombre: "CarlosJ",   Juegos: 303, Ganados: 180, Perdidos: 123,  Dif:  6,  Porcentaje: 595, diasPerfectos: 9165458},
  { Pos: 4 ,Nombre: "Kleydi",    Juegos: 302, Ganados: 175, Perdidos: 127,  Dif:  11, Porcentaje: 580, diasPerfectos: 9},
  { Pos: 5 ,Nombre: "Daniel",    Juegos: 303, Ganados: 173, Perdidos: 130,  Dif:  13, Porcentaje: 570, diasPerfectos: 1},
  { Pos: 6 ,Nombre: "Erycherd",  Juegos: 302, Ganados: 167, Perdidos: 135,  Dif:  19, Porcentaje: 550, diasPerfectos: 5},
  { Pos: 7 ,Nombre: "Christian", Juegos: 303, Ganados: 166, Perdidos: 137,  Dif:  20, Porcentaje: 545, diasPerfectos: 17},
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