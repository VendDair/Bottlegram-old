import {writable} from "svelte/store"

export const new_post = writable(false)
export const url = writable(undefined)
export const init = writable(false)
