'use client';

import * as React from 'react';
import { Card, CardContent } from '@/components/ui/card';

export default function InternshipsPage() {
  const internships = [
    {
      id: 1,
      title: 'NASA Pathways Internships',
      url: 'https://nasa.gov/careers/pathways',
      description:
        'Hands-on experience and training in engineering, science, and technology fields. Gain real-world experience while contributing to meaningful projects at NASA.',
    },
    {
      id: 2,
      title: 'NASA Office of STEM Engagement',
      url: 'https://nasa.gov/stem/internships',
      description:
        'Opportunities for students in STEM fields to work on real-world projects. Engage with professionals and build your career with NASA.',
    },
    {
      id: 3,
      title: 'NASA DEVELOP Program',
      url: 'https://develop.larc.nasa.gov',
      description:
        'Engaging students in Earth science research to address environmental challenges. Collaborate with a team to create impactful solutions.',
    },
    {
      id: 4,
      title: 'Lunar Exploration Program',
      url: 'https://nasa.gov/lunar-program',
      description:
        'Join NASA’s efforts to explore the Moon and develop cutting-edge technologies for lunar exploration.',
    },
    {
      id: 5,
      title: 'Astrobiology and the Search for Life',
      url: 'https://nasa.gov/astrobiology',
      description:
        'Explore the possibilities of life beyond Earth and conduct research in extreme environments to uncover new knowledge.',
    },
  ];

  return (
    <div className='relative z-20 flex flex-col items-center justify-center min-h-screen'>
      {/* Top-left header */}
      <h1 className='absolute top-4 left-4 text-2xl font-bold text-white'>
        Internships
      </h1>

      {/* Scrollable List of Boxes */}
      <div className='w-full max-w-4xl h-[70vh] overflow-y-auto space-y-4 mt-8'>
        {internships.map((internship) => (
          <Card
            key={internship.id}
            className='bg-gray-800 text-white shadow-md rounded-lg'
          >
            <CardContent className='p-4 space-y-2 max-h-40 overflow-y-auto'>
              {/* Title */}
              <h2 className='text-xl font-bold'>{internship.title}</h2>
              {/* URL */}
              <a
                href={internship.url}
                target='_blank'
                rel='noopener noreferrer'
                className='text-blue-500 underline hover:text-blue-300 text-sm'
              >
                {internship.url}
              </a>
              {/* Description */}
              <p className='text-sm text-gray-400'>{internship.description}</p>
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  );
}
