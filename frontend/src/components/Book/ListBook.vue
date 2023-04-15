<template lang="html">
    <div class="container">
        <div class="row">
            <div class="col text-center">
                <h2> Listado de libros</h2>
                <div class="col-md-12">
                    <b-table striped hover :items="books" :fields="fields">

                    </b-table>
                </div>
            </div>
        </div>
    </div>

</template>

<script>
import axios from 'axios'
export default{
    data(){
        return{
            fields:[
                {key: 'title', label: 'Titulo'},
                {key: 'description', label: 'Descripcion'},
            ],
            books:[]
        }
    },
    methods:{
        getBooks(){
            const path = 'http://127.0.0.1:8000/api/v1.0/books/'
            axios.get(path).then((response) => {
                this.books = response.data
            })
            .catch((error) =>{
                console.log(error)
            })
        }
    },
    created(){
        this.getBooks()
    }
    
}
</script>

<style lang="css" scoped>

</style>