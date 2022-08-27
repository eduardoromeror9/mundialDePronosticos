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
  { Pos: 1 ,Nombre: "Eduardo",   Juegos: 256, Ganados: 153, Perdidos: '103', Dif: '-',  Porcentaje: '595', diasPerfectos: 'noSabe' },
  { Pos: 2 ,Nombre: "CarlosJ",   Juegos: 256, Ganados: 153, Perdidos: '103', Dif: '-',  Porcentaje: '595', diasPerfectos: 'Dice que 1765'},
  { Pos: 3 ,Nombre: "Steven",    Juegos: 256, Ganados: 152, Perdidos: '104', Dif:  1,   Porcentaje: '590', diasPerfectos: 'noSabe' },
  { Pos: 4 ,Nombre: "Kleydi",    Juegos: 256, Ganados: 151, Perdidos: '105', Dif:  2,   Porcentaje: '585', diasPerfectos: 'noSabe' },
  { Pos: 5 ,Nombre: "Daniel",    Juegos: 256, Ganados: 143, Perdidos: '113', Dif:  10,  Porcentaje: '560', diasPerfectos: 'noSabe'},
  { Pos: 6 ,Nombre: "Christian", Juegos: 256, Ganados: 137, Perdidos: '119', Dif:  16,  Porcentaje: '535', diasPerfectos: 'noSabe'},
  { Pos: 7 ,Nombre: "Erycherd",  Juegos: 256, Ganados: 135, Perdidos: '121', Dif:  18,  Porcentaje: '525', diasPerfectos: 'noSabe'}
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