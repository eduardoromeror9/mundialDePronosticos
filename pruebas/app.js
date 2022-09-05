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
  { Pos: 1 ,Nombre: "Eduardo",   Juegos: 271, Ganados: 164, Perdidos: 107,  Dif: '-',  Porcentaje: 605, diasPerfectos: 5},
  { Pos: 2 ,Nombre: "Steven",    Juegos: 271, Ganados: 163, Perdidos: 108,  Dif:  1,   Porcentaje: 600, diasPerfectos: 4},
  { Pos: 3 ,Nombre: "CarlosJ",   Juegos: 271, Ganados: 162, Perdidos: 109,  Dif:  2,   Porcentaje: 595, diasPerfectos: 9165458},
  { Pos: 4 ,Nombre: "Kleydi",    Juegos: 271, Ganados: 158, Perdidos: 113,  Dif:  6,   Porcentaje: 585, diasPerfectos: 3},
  { Pos: 6 ,Nombre: "Christian", Juegos: 271, Ganados: 148, Perdidos: 123,  Dif:  16,  Porcentaje: 545, diasPerfectos: 1},
  { Pos: 7 ,Nombre: "Erycherd",  Juegos: 271, Ganados: 143, Perdidos: 127,  Dif:  21,  Porcentaje: 525, diasPerfectos: 2},
  { Pos: 'X' ,Nombre: "--------",  Juegos:  '--------', Ganados: '--------', Perdidos: '--------',  Dif:  '--------',  Porcentaje: '--------', diasPerfectos: '--------'},
  { Pos: 'X' ,Nombre: "NULOS",  Juegos:  'NULOS', Ganados: 'NULOS', Perdidos: 'NULOS',  Dif:  'NULOS',  Porcentaje: 'NULOS', diasPerfectos: 'NULOS'},
  { Pos: 5 ,Nombre: "Daniel",    Juegos: 271, Ganados: 153, Perdidos: 118,  Dif:  11,  Porcentaje: 565, diasPerfectos: 2},

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