import { ErrorComponentProps } from "@tanstack/react-router";

export const ErrorComponent = ({ error, reset, info }: ErrorComponentProps) => {
    return (
        <div className='min-h-screen bg-black/50 backdrop-blur-3xl flex flex-col items-center justify-center'>
            <p>{error.message}</p>
            <p>{info?.componentStack}</p>
            <button className="bg-black text-white p-3 px-10 cursor-pointer focus:bg-black/50" onClick={reset}>Reset</button>
        </div>
    )
}