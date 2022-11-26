<template>
    <div>
        <img :src="avatar" :alt="descricao">
        <MudarImagem @mudar-imagem="trocarImagem" />
    </div>
</template>

<script>
import Reutilizacao from './Reutilizacao.vue'
import MudarImagem from './MudarImagem.vue';

export default {
    name: 'Picture',
    data() {
        return {
            avatar: "/img/avatar.png",
            descricao: "Matheus Battisti"
        }
    },
    components: {
        Reutilizacao,
        MudarImagem
    },
    methods: {
        trocarImagem() {
            console.log("Opa")
            this.avatar = "/img/avatar2.png"
        }
    }
}
</script>