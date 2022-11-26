<template>
    <div>
        <button @click="$emit('MudarImagem')">Trocar imagem de perfil</button>
    </div>    
</template>

<script>
export default {
    name: 'MudarImagem',
    emits: ['MudarImagem']
}
</script>