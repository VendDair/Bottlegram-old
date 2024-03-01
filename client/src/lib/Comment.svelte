<script>
  export let text
  export let name
</script>

<div class="container">
  <p>{name}: {text}</p>
</div>

<style lang="scss">
  .container {
    width: 100%;
    background-color: rgb(40, 40, 40);
    display: flex;
    justify-content: center;
    align-items: center;
    flex-wrap: wrap;
    margin: 10px 0;
    p {
      color: white;
      word-wrap: anywhere;
      padding: 0 10px;
      font-size: calc(1vmin + .6pc);
    }
  }
</style>
