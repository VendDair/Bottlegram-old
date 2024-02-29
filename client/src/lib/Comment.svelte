<script>
  export let text
</script>

<div class="container">
  <p>{text}</p>
</div>

<style lang="scss">
  .container {
    width: 100%;
    background-color: red;
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 10px 0;
    p {
      color: white;
    }
  }
</style>
