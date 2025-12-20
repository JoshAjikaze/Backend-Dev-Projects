import { createFileRoute, Link } from '@tanstack/react-router'

export const Route = createFileRoute('/users')({
  component: RouteComponent,
  loader: async () => {

    const res = await fetch(`https://jsonplaceholder.typicode.com/users/`)
    const users = await res.json()

    return { users }
  }
})

function RouteComponent() {
  const { users } = Route.useLoaderData()
  console.log(users)
  return <div>
    <div className="container mx-auto">
      <p className="text-2xl font-bold">
        All Users
      </p>
      <table className='w-full border-collapse border border-gray-300'>
        <thead>
          <tr>
            <th className='text-left p-5 border border-gray-300'>Name</th>
            <th className='text-left p-5 border border-gray-300'>Username</th>
            <th className='text-left p-5 border border-gray-300'>Email</th>
            <th className='text-left p-5 border border-gray-300'>Phone</th>
            <th className='text-left p-5 border border-gray-300'>Website</th>
          </tr>
        </thead>
        <tbody>
          {
            users.map((user: any) => (
              <tr key={user.id} className='hover:bg-gray-50'>
                <td className="p-5 border border-gray-300"><Link to="/user/$id" params={{ id: user.id }}> {user.name} </Link></td>
                <td className="p-5 border border-gray-300">{user.username}</td>
                <td className="p-5 border border-gray-300">{user.email}</td>
                <td className="p-5 border border-gray-300">{user.phone}</td>
                <td className="p-5 border border-gray-300">{user.website}</td>
              </tr>
            ))
          }
        </tbody>
      </table>
    </div>
  </div>
}
