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
  { Pos: 1 ,Nombre: "Eduardo",   Juegos: 259, Ganados: 155, Perdidos: 104,  Dif: '-',  Porcentaje: 600, diasPerfectos: 'noSabe' },
  { Pos: 2 ,Nombre: "CarlosJ",   Juegos: 259, Ganados: 153, Perdidos: 106,  Dif:  2,   Porcentaje: 590, diasPerfectos: 'Dice que 1765'},
  { Pos: 3 ,Nombre: "Steven",    Juegos: 259, Ganados: 152, Perdidos: 107,  Dif:  3,   Porcentaje: 585, diasPerfectos: 'noSabe' },
  { Pos: 4 ,Nombre: "Kleydi",    Juegos: 259, Ganados: 151, Perdidos: 108,  Dif:  4,   Porcentaje: 580, diasPerfectos: 'noSabe' },
  { Pos: 5 ,Nombre: "Daniel",    Juegos: 259, Ganados: 144, Perdidos: 115,  Dif:  11,  Porcentaje: 555, diasPerfectos: 'noSabe'},
  { Pos: 6 ,Nombre: "Christian", Juegos: 259, Ganados: 138, Perdidos: 121,  Dif:  17,  Porcentaje: 530, diasPerfectos: 'noSabe'},
  { Pos: 7 ,Nombre: "Erycherd",  Juegos: 259, Ganados: 135, Perdidos: 124,  Dif:  20,  Porcentaje: 520, diasPerfectos: 'noSabe'}
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