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

export default function InternshipsPage() {
  // OSTEM Internship Entries
  const ostemInternships = [
    {
      id: 1,
      title: 'OSTEM Internship 1',
      url: 'https://nasa.gov/ostem1',
      description:
        'Develop critical skills in engineering, science, and technology at NASA.',
    },
    {
      id: 2,
      title: 'OSTEM Internship 2',
      url: 'https://nasa.gov/ostem2',
      description:
        'Engage in research opportunities to contribute to NASA’s space missions.',
    },
    {
      id: 3,
      title: 'OSTEM Internship 3',
      url: 'https://nasa.gov/ostem3',
      description: 'Collaborate with scientists and engineers on innovative projects.',
    },
  ];

  // PATHWAYS Internship Entries
  const pathwaysInternships = [
    {
      id: 1,
      title: 'PATHWAYS Internship 1',
      url: 'https://nasa.gov/pathways1',
      description: 'Explore long-term career opportunities with hands-on experience.',
    },
    {
      id: 2,
      title: 'PATHWAYS Internship 2',
      url: 'https://nasa.gov/pathways2',
      description: 'Work on groundbreaking projects that support NASA’s goals.',
    },
    {
      id: 3,
      title: 'PATHWAYS Internship 3',
      url: 'https://nasa.gov/pathways3',
      description: 'Gain experience in leadership, innovation, and collaboration.',
    },
  ];

  return (
    <div className='relative z-20 flex flex-col items-center justify-center min-h-screen'>
      {/* Top-left header */}
      <h1 className='absolute top-4 left-4 text-2xl font-bold text-white'>
        Internships
      </h1>

      {/* OSTEM Carousel */}
      <div className='w-full max-w-4xl mt-8'>
        <h2 className='text-xl font-bold text-white mb-4'>OSTEM Internships</h2>
        <Carousel
          className='flex flex-col'
          opts={{
            axis: 'y', // Vertical carousel for OSTEM
            align: 'start',
          }}
        >
          <CarouselContent className='space-y-4'>
            {ostemInternships.map((internship) => (
              <CarouselItem key={internship.id} className='h-[300px]'>
                <Card className='bg-gray-800 text-white shadow-md rounded-lg h-full'>
                  <CardContent className='p-6 space-y-4 overflow-y-auto'>
                    <h2 className='text-lg font-bold'>{internship.title}</h2>
                    <a
                      href={internship.url}
                      target='_blank'
                      rel='noopener noreferrer'
                      className='text-blue-500 underline hover:text-blue-300 text-sm'
                    >
                      {internship.url}
                    </a>
                    <p className='text-sm text-gray-400'>{internship.description}</p>
                  </CardContent>
                </Card>
              </CarouselItem>
            ))}
          </CarouselContent>
          <CarouselPrevious className='text-gray-400 hover:text-white' />
          <CarouselNext className='text-gray-400 hover:text-white' />
        </Carousel>
      </div>

      {/* PATHWAYS Carousel */}
      <div className='w-full max-w-4xl mt-16'>
        <h2 className='text-xl font-bold text-white mb-4'>PATHWAYS Internships</h2>
        <Carousel
          className='flex flex-col'
          opts={{
            axis: 'y', // Vertical carousel for PATHWAYS
            align: 'start',
          }}
        >
          <CarouselContent className='space-y-4'>
            {pathwaysInternships.map((internship) => (
              <CarouselItem key={internship.id} className='h-[300px]'>
                <Card className='bg-gray-800 text-white shadow-md rounded-lg h-full'>
                  <CardContent className='p-6 space-y-4 overflow-y-auto'>
                    <h2 className='text-lg font-bold'>{internship.title}</h2>
                    <a
                      href={internship.url}
                      target='_blank'
                      rel='noopener noreferrer'
                      className='text-blue-500 underline hover:text-blue-300 text-sm'
                    >
                      {internship.url}
                    </a>
                    <p className='text-sm text-gray-400'>{internship.description}</p>
                  </CardContent>
                </Card>
              </CarouselItem>
            ))}
          </CarouselContent>
          <CarouselPrevious className='text-gray-400 hover:text-white' />
          <CarouselNext className='text-gray-400 hover:text-white' />
        </Carousel>
      </div>
    </div>
  );
}
