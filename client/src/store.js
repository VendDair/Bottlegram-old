import {writable} from "svelte/store"

export const new_post = writable(false)
export const url = writable(undefined)
export const init = writable(false)
export const comments_amount = writable(0)
export const name_temp = writable("")
