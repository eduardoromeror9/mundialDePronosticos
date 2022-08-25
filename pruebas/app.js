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
  { Pos: 1 ,Nombre: "Eduardo",   Juegos: 253, Ganados: 151, Perdidos: '102', Dif: '-',  Porcentaje: '595', diasPerfectos: 'noSabe' },
  { Pos: 2 ,Nombre: "Steven",    Juegos: 253, Ganados: 150, Perdidos: '103', Dif:  1,   Porcentaje: '590', diasPerfectos: 'noSabe' },
  { Pos: 3 ,Nombre: "CarlosJ",   Juegos: 253, Ganados: 150, Perdidos: '103', Dif:  1,   Porcentaje: '590', diasPerfectos: 'Dice que 1765'},
  { Pos: 4 ,Nombre: "Kleydi",    Juegos: 253, Ganados: 149, Perdidos: '104', Dif:  2,   Porcentaje: '585', diasPerfectos: 'noSabe' },
  { Pos: 5 ,Nombre: "Daniel",    Juegos: 253, Ganados: 140, Perdidos: '113', Dif:  11,  Porcentaje: '555', diasPerfectos: 'noSabe'},
  { Pos: 6 ,Nombre: "Christian", Juegos: 253, Ganados: 136, Perdidos: '117', Dif:  15,  Porcentaje: '540', diasPerfectos: 'noSabe'},
  { Pos: 7 ,Nombre: "Erycherd",  Juegos: 253, Ganados: 133, Perdidos: '120', Dif:  18,  Porcentaje: '525', diasPerfectos: 'noSabe'}
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