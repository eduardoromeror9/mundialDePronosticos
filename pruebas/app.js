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
  { Pos: 1 ,Nombre: "Eduardo",   Juegos: 280, Ganados: 171, Perdidos: 109,  Dif: '-',  Porcentaje: 610, diasPerfectos: 5},
  { Pos: 2 ,Nombre: "Steven",    Juegos: 280, Ganados: 169, Perdidos: 111,  Dif:  2,   Porcentaje: 600, diasPerfectos: 4},
  { Pos: 3 ,Nombre: "CarlosJ",   Juegos: 280, Ganados: 167, Perdidos: 113,  Dif:  4,   Porcentaje: 595, diasPerfectos: 9165458},
  { Pos: 4 ,Nombre: "Kleydi",    Juegos: 280, Ganados: 163, Perdidos: 117,  Dif:  8,   Porcentaje: 580, diasPerfectos: 3},
  { Pos: 5 ,Nombre: "Daniel",    Juegos: 280, Ganados: 156, Perdidos: 124,  Dif:  15,  Porcentaje: 560, diasPerfectos: 2},
  { Pos: 6 ,Nombre: "Christian", Juegos: 280, Ganados: 153, Perdidos: 127,  Dif:  18,  Porcentaje: 545, diasPerfectos: 1},
  { Pos: 7 ,Nombre: "Erycherd",  Juegos: 280, Ganados: 149, Perdidos: 130,  Dif:  22,  Porcentaje: 530, diasPerfectos: 2},
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