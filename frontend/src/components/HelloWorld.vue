<template lang="pug">
  .hello
    h1 {{ msg }}
</template>

<script>
import apiUrl from "../apiUrl";

export default {
  name: "HelloWorld",
  created() {
    this.axios.get(apiUrl.ping).then((response) => {
      console.log(response);
    });
  },
  props: {
    msg: String
  }
};
</script>
