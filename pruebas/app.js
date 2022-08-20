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
  { Pos: 1 ,Nombre: "Eduardo",   Juegos: 244, Ganados: 144, Perdidos: '100', Dif: '-', Porcentaje: '590', diasPerfectos: 'noSabe' },
  { Pos: 2 ,Nombre: "Steven",    Juegos: 244, Ganados: 144, Perdidos: '100', Dif: '-', Porcentaje: '590', diasPerfectos: 'noSabe' },
  { Pos: 4 ,Nombre: "CarlosJ",   Juegos: 244, Ganados: 144, Perdidos: '100', Dif: '-', Porcentaje: '590', diasPerfectos: 'Dice que 1765'},
  { Pos: 3 ,Nombre: "Kleydi",    Juegos: 244, Ganados: 143, Perdidos: '101', Dif:  1,  Porcentaje: '585', diasPerfectos: 'noSabe' },
  { Pos: 5 ,Nombre: "Daniel",    Juegos: 244, Ganados: 135, Perdidos: '109', Dif:  9,  Porcentaje: '555', diasPerfectos: 'noSabe'},
  { Pos: 7 ,Nombre: "Erycherd",  Juegos: 244, Ganados: 130, Perdidos: '114', Dif:  14, Porcentaje: '535', diasPerfectos: 'noSabe'},
  { Pos: 6 ,Nombre: "Christian", Juegos: 244, Ganados: 129, Perdidos: '115', Dif:  15, Porcentaje: '530', diasPerfectos: 'noSabe'}
];

let legend = 
  `\n                         🔥🔥 INFORMACION IMPORTANTE 🔥🔥
                              Don Eduardo Romero,
                              mejor conocido como
                              el KING de los PRONOSTICOS
                              ES EL VIGENTE CAMPEON
                                     HASTA QUE
                              SE DEMUESTRE LO CONTRARIO
  \n`
  console.log(legend.yellow.bold);

let info =
 `                         🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊
                         🧊                                🧊
                         🧊      CarlosJ a la NEVERA       🧊
                         🧊      Steven a la NEVERA        🧊  
                         🧊      Kleydi a la NEVERA        🧊  
                         🧊                                🧊
                         🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊 \n`

console.log(info.blue.bold);

table(test);