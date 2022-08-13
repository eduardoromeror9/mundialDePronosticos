// function Employee(firstName, lastName, email, juegos) {
//   this.firstName = firstName;
//   this.lastName = lastName;
//   this.email = email;
//   this.juegos = juegos;
// }
// var A = new Employee("Peter", "Eze", "peter@test.com");
// var B = new Employee("Chris", "Nwamba", "chris@test.com");
// var C = new Employee("William", "Imoh", "william@test.com");
// var D = new Employee(72,5,4);

// console.table([A, B, C, D]);

function competidores(Nombre, Juegos, Porcentaje) {
  this.Nombre = Nombre;
  this.Juegos = Juegos;
  this.Porcentaje = Porcentaje;
}



var team = {}

  team.LIDERABSOLUTO = new competidores("Eduardo",     "100-30",  600);
  team.Segundo       = new competidores("Steven",      "100-30",  600);
  team.Tercero       = new competidores("Kleydi",      "100-30",  600);
  team.Cuarto        = new competidores("Carlos Jose", "100-30",  600);
  team.Quinto        = new competidores("Daniel",      "100-30",  600);
  team.Sexto         = new competidores("Erycherd",    "100-30",  600);
  team.Séptimo       = new competidores("Christian",   "100-30",  600);
  team.Lejos         = new competidores("Jhon",        "100-30",  600);

// console.table(team);

// const modifiedArr = teams.map [elem => {

//   return {
  
//   nombre: elem.name,
  
//   partidos ganados: elem.matchesWon,
  
//   partidos perdidos: elem.matchesLost,
  
//   puntos: elem.points,
  
//   goles a favor: elem.goalsFor,
  
//   goles en contra: elem.goalsAgainst,
  
//   }
  
//   }


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
  { Pos: 1 ,Nombre: "Eduardo",   Juegos: 232, Ganados: 138, Perdidos: '94',  Dif: '-', Porcentaje: '595', diasPerfectos: 'noSabe' },
  { Pos: 2 ,Nombre: "Steven",    Juegos: 232, Ganados: 137, Perdidos: '95',  Dif:  1, Porcentaje: '590', diasPerfectos:  'noSabe' },
  { Pos: 3 ,Nombre: "Kleydi",    Juegos: 232, Ganados: 136, Perdidos: '96',  Dif:  2, Porcentaje: '585', diasPerfectos:  'noSabe' },
  { Pos: 4 ,Nombre: "CarlosJ",   Juegos: 232, Ganados: 136, Perdidos: '96',  Dif:  2, Porcentaje: '585', diasPerfectos: 'Dice que 97'},
  { Pos: 5 ,Nombre: "Daniel",    Juegos: 232, Ganados: 129, Perdidos: '103', Dif:  9, Porcentaje: '555', diasPerfectos:  'noSabe'},
  { Pos: 6 ,Nombre: "Christian", Juegos: 232, Ganados: 122, Perdidos: '109', Dif:  16, Porcentaje: '525', diasPerfectos: 'noSabe'},
  { Pos: 7 ,Nombre: "Erycherd",  Juegos: 232, Ganados: 122, Perdidos: '110', Dif:  16, Porcentaje: '525', diasPerfectos: 'noSabe'}
];

let legend = 
  `\n                      🔥🔥 INFORMACION IMPORTANTE 🔥🔥
                           Don Eduardo Romero,
                           mejor conocido como
                           el KING de los PRONOSTICOS
                           ES EL VIGENTE CAMPEON
                                  HASTA QUE
                           SE DEMUESTRE LO CONTRARIO
  \n`
  console.log(legend.yellow.bold);

let info =
 `                      🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊
                      🧊                                🧊
                      🧊      CarlosJ a la NEVERA       🧊
                      🧊      Steven a la NEVERA        🧊  
                      🧊      Kleydi a la NEVERA        🧊  
                      🧊                                🧊
                      🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊 \n`

console.log(info.blue.bold);

table(test);