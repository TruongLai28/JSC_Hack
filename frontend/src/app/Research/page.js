'use client';

import * as React from 'react';
import { Card, CardContent } from '@/components/ui/card';

export default function ResearchPage() {
  const researchEntries = [
    {
      id: 1,
      title: 'Understanding Space Weather',
      url: 'https://nasa.gov/space-weather',
      description:
        'Exploring the effects of solar activity on Earth and space missions.',
    },
    {
      id: 2,
      title: 'Mars Rover Missions',
      url: 'https://nasa.gov/mars-rovers',
      description:
        'Detailed insights into the journey of NASA’s rovers on Mars.',
    },
    {
      id: 3,
      title: 'Astrobiology and the Search for Life',
      url: 'https://nasa.gov/astrobiology',
      description:
        'Examining the possibilities of life beyond Earth in extreme environments.',
    },
  ];

  return (
    <div className='relative z-20 flex flex-col items-center justify-center min-h-screen'>
      {/* Top-left header */}
      <h1 className='absolute top-4 left-4 text-2xl font-bold text-white'>
        Research
      </h1>

      {/* Research Entries */}
      <div className='w-full max-w-4xl space-y-4 mt-8'>
        {researchEntries.map((entry) => (
          <Card
            key={entry.id}
            className='bg-gray-800 text-white shadow-md rounded-lg'
          >
            <CardContent className='p-4 space-y-2'>
              {/* Title */}
              <h2 className='text-lg font-bold'>{entry.title}</h2>
              {/* URL */}
              <a
                href={entry.url}
                target='_blank'
                rel='noopener noreferrer'
                className='text-blue-500 underline hover:text-blue-300 text-sm'
              >
                {entry.url}
              </a>
              {/* Description */}
              <p className='text-sm text-gray-400'>{entry.description}</p>
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  );
}
