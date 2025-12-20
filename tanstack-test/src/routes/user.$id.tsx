import { getGreetings } from '@/api/getGreetings'
import { getServerTime } from '@/api/getServerTime'
import { ErrorComponent } from '@/components/ErrorComponent'
import { createFileRoute } from '@tanstack/react-router'

export const Route = createFileRoute('/user/$id')({
  component: RouteComponent,
  notFoundComponent: () => <div>Not Found</div>,
  loader: async ({ params }) => {
    // if (Number(params.id) > 10) {
    //   throw new Error('No user above 10 allowed!')
    // }

    const resp = { userName: "John Doe" }

    const res = await fetch(`https://jsonplaceholder.typicode.com/users/${params.id}`)
    const user = await res.json()

    if (!user.id) {
      throw new Error("No User is found")
    }

    const time = await getServerTime()
    const currentGreeting = await getGreetings()

    return { resp, user, time, currentGreeting }
  },
  pendingComponent: () => <div>Loading...</div>,
  errorComponent: ({ error, reset }) => <ErrorComponent error={error} reset={reset} />,
})

function RouteComponent() {

  const { 
    // resp,
    user,
    time, 
    currentGreeting
  } = Route.useLoaderData()


  return <div>
    <div className="container mx-auto">
      <h1 className='font-bold text-2xl py-3'>Current user</h1>
      <p>{time}</p>
      <p>{currentGreeting}</p>
      <table className='flex gap-1'>
        <th className='flex flex-col gap-y-1'>
          <td className='border p-5 text-left'>Name</td>
          <td className='border p-5 text-left'>Username</td>
          <td className='border p-5 text-left'>Email</td>
          <td className='border p-5 text-left'>Phone</td>
          <td className='border p-5 text-left'>Website</td>
        </th>
        <tbody className='flex flex-col gap-y-1'>
          <td className='border p-5 text-left'>{user.name}</td>
          <td className='border p-5 text-left'>{user.username}</td>
          <td className='border p-5 text-left'>{user.email}</td>
          <td className='border p-5 text-left'>{user.phone}</td>
          <td className='border p-5 text-left'>{user.website}</td>
        </tbody>
      </table>
    </div>
  </div>
}
