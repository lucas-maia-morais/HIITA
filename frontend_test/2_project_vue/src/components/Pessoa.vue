<template>
    <div>
        <h2>Essa é a descrição da pessoa: {{ nome }}</h2>
        <Info :email="email" :esta_trabalhando="esta_trabalhando"/>
        <Form />
    </div>
</template>

<script>
    import Form from './Form.vue'
    import Info from './Info.vue'
    
    export default {
    components: { Info, Form },
    name: 'Pessoa',
    data() {
        return {
            nome: "Matheus",
            email: "matheus2@email.com",
            esta_trabalhando: false
        }
    }
}
</script>