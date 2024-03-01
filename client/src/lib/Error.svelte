<script>
  import jQuery from "jquery";
  import {get_current_component} from 'svelte/internal'
  const THISComponent = get_current_component()
  export let text
  text = "Error: " + text

  var disapear = false

  jQuery("main").on("animationend", function() {
    setTimeout(function () {
      disapear = true
    }, 2000)
    setTimeout(function() {
      THISComponent.$destroy()
    }, 4000)
  })
</script>

<main class="{disapear ? 'disapear' : ''}">
  <p>{text}</p>
</main>

<style lang="scss">
  @keyframes apear {
    0% {
      top: -100px;
  }
    100% {
      top: 10px;
  }
  }
  @keyframes disapears {
    from { top: 10px;}
    to { top: -100px}
  }

  .disapear {
    animation: disapears ease 1s alternate forwards;
  }

  main {
    background-color: red;
    border-radius: 10px;
    position: absolute;
    left: 50%;
    top: -100px;
    font-family: "Tahoma", sans-serif;
    font-weight: bold;
    display: flex;
    justify-content: center;
    align-items: center;
    transform: translateX(-50%);
    color: white;
    animation: apear ease 1s alternate forwards;
    z-index: 100;
    padding: 0 1dvw;
    p {
      text-align: center;
    }
  }
  @media screen and (orientation:portrait) {
    main {
      width: 90dvw;
    }
  }

</style>
