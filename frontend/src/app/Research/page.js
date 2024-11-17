'use client';

import * as React from 'react';
import { Card, CardContent } from '@/components/ui/card';
import {
  Carousel,
  CarouselContent,
  CarouselItem,
  CarouselNext,
  CarouselPrevious,
} from '@/components/ui/carousel';

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
    {
      id: 4,
      title: 'Lunar Exploration Program',
      url: 'https://nasa.gov/lunar-program',
      description:
        'Join NASA’s efforts to explore the Moon and develop cutting-edge technologies for lunar exploration.',
    },
    {
      id: 5,
      title: 'Exploring Exoplanets',
      url: 'https://nasa.gov/exoplanets',
      description:
        'Investigating planets outside our solar system and their potential to support life.',
    },
  ];

  return (
    <div className='relative z-20 flex flex-col items-center justify-center min-h-screen'>
      {/* Top-left header */}
      <h1 className='absolute top-4 left-4 text-2xl font-bold text-white'>
        Research
      </h1>

      {/* Horizontal Carousel */}
      <div className='w-full max-w-6xl flex flex-col relative'>
        <Carousel
          className='flex'
          opts={{
            axis: 'x', // Make carousel horizontal
            align: 'start', // Align items at the start
          }}
        >
          {/* Carousel Content */}
          <CarouselContent className='flex gap-4'>
            {researchEntries.map((entry) => (
              <CarouselItem
                key={entry.id}
                className='flex-shrink-0 w-[50%] md:w-[30%]'
              >
                <Card className='bg-gray-800 text-white shadow-md rounded-lg h-full'>
                  <CardContent className='p-6 space-y-4 overflow-y-auto h-[300px]'>
                    <h2 className='text-lg font-bold'>{entry.title}</h2>
                    <a
                      href={entry.url}
                      target='_blank'
                      rel='noopener noreferrer'
                      className='text-blue-500 underline hover:text-blue-300 text-sm'
                    >
                      {entry.url}
                    </a>
                    <p className='text-sm text-gray-400'>{entry.description}</p>
                  </CardContent>
                </Card>
              </CarouselItem>
            ))}
          </CarouselContent>

          {/* Navigation Arrows */}
          <CarouselPrevious className='absolute left-2 top-1/2 transform -translate-y-1/2 text-gray-400 hover:text-white' />
          <CarouselNext className='absolute right-2 top-1/2 transform -translate-y-1/2 text-gray-400 hover:text-white' />
        </Carousel>
      </div>
    </div>
  );
}
