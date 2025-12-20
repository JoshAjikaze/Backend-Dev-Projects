import { createServerFn } from "@tanstack/react-start";
import { getuser } from "./getUser";

export const getGreetings = createServerFn().handler(async() => {
    const user = await getuser()
    return `Hello ${user.name}`
})