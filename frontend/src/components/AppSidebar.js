import {
  HomeIcon,
  RocketLaunchIcon,
  AcademicCapIcon,
  BeakerIcon,
  CalendarIcon,
} from '@heroicons/react/24/outline';

export function AppSidebar() {
  const menuItems = [
    { name: 'Home', icon: <HomeIcon className='h-6 w-6' />, href: '/' },
    {
      name: 'Launch',
      icon: <RocketLaunchIcon className='h-6 w-6' />,
      href: '/launch',
    },
    {
      name: 'Internships',
      icon: <AcademicCapIcon className='h-6 w-6' />,
      href: '/internships',
    },
    {
      name: 'Research',
      icon: <BeakerIcon className='h-6 w-6' />,
      href: '/research',
    },
    {
      name: 'Events',
      icon: <CalendarIcon className='h-6 w-6' />,
      href: '/events',
    },
  ];

  return (
    <aside className='bg-slate-800 text-white w-64 h-screen fixed top-0 left-0 p-4 flex flex-col'>
      <div className='mb-8 text-xl font-bold'>Rocket Launch xD</div>
      <nav>
        {menuItems.map((item) => (
          <a
            key={item.name}
            href={item.href}
            className='flex items-center p-2 mb-2 rounded hover:bg-blue-700 transition'
          >
            {item.icon}
            <span className='ml-4'>{item.name}</span>
          </a>
        ))}
      </nav>
    </aside>
  );
}
