class persona {
    constructor(nombre, edad, sexo, peso, altura) {
        this.nombre = nombre;
        this.edad = edad;
        this.sexo = sexo;
        this.peso = peso;
        this.altura = altura;
        
    }
    caminar() {
        console.log("Estoy caminando");
    }
    correr() {
        console.log("Estoy corriendo");
    }
    identificacion() {
        console.log(`Hola soy ${this.nombre} tengo ${this.edad} años, soy ${this.sexo}, peso ${this.peso} kg y mido ${this.altura} mts`);
    }
}
class Estudiante {
    constructor(nombre, curso, calificacion, faltas,asistencia){
        this.nombre = nombre;
        this.curso = curso;
        this.calificacion = calificacion;
        this.faltas = faltas;
        this.asistencia = asistencia;
    }
    faltar(){
        this.faltas=this.faltas+1;
    }
    asistir(){
        this.asistencia=this.asistencia+1;
    }

    promedio(calificacion){

        this.calificacion = this.calificacion + calificacion/2;
        return `El promedio de ${this.nombre} es ${this.calificacion}`;
    }

}