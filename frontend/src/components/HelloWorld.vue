<template lang="pug">
  .hello
    h1 {{ msg }}
</template>

<script>
export default {
  name: "HelloWorld",
  created() {
    this.axios.get("/ping").then((response) => {
      console.log(response);
    });
  },
  props: {
    msg: String
  }
};
</script>
