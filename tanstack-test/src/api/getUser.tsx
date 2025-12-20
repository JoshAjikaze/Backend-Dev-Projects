import { createServerFn } from "@tanstack/react-start";

export const getuser = createServerFn().handler(
    async () => {
        const name = "Joshua"
        const age = 25
        const isEmployed = true

        return { name, age, isEmployed }
    }
)