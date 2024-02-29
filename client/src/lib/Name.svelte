<script>
  import {generate} from "random-words"
  if (localStorage.getItem("name") == null)
  {
    let new_name = ""
    let words = generate({min:3, max: 5, minLength: 1, maxLength: 3})
    words.forEach(element => {
      new_name += element + "_"
    })
    localStorage.setItem("name", new_name)
  }
</script>

<main class="name">
  {localStorage.getItem("name")}
</main>

<style lang="scss">
  main.name {
    color: white;
  }
</style>
