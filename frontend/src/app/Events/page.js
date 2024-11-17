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

export default function EventsPage() {
  const events = [
    {
      id: 1,
      title: 'Event 1',
      url: 'https://example.com/event1',
      description: 'Details about Event 1.',
    },
    {
      id: 2,
      title: 'Event 2',
      url: 'https://example.com/event2',
      description: 'Details about Event 2.',
    },
    {
      id: 3,
      title: 'Event 3',
      url: 'https://example.com/event3',
      description: 'Details about Event 3.',
    },
    {
      id: 4,
      title: 'Event 4',
      url: 'https://example.com/event4',
      description: 'Details about Event 4.',
    },
    {
      id: 5,
      title: 'Event 5',
      url: 'https://example.com/event5',
      description: 'Details about Event 5.',
    },
  ];

  return (
    <div className='relative z-20 flex flex-col items-center justify-center min-h-screen'>
      {/* Top-left header */}
      <h1 className='absolute top-4 left-4 text-2xl font-bold text-white'>
        Events
      </h1>

      {/* Carousel */}
      <div className='w-full max-w-6xl'>
        <Carousel
          opts={{
            align: 'start', // Align items to the start
          }}
        >
          <CarouselContent>
            {events.map((event) => (
              <CarouselItem
                key={event.id}
                className='md:basis-1/2 lg:basis-1/3'
              >
                <div className='p-2'>
                  <Card className='bg-gray-800 text-white shadow-md rounded-lg'>
                    <CardContent className='p-4 space-y-4'>
                      <h2 className='text-lg font-bold'>{event.title}</h2>
                      <p className='text-sm text-gray-400'>
                        {event.description}
                      </p>
                      <a
                        href={event.url}
                        target='_blank'
                        rel='noopener noreferrer'
                        className='text-blue-500 underline hover:text-blue-300'
                      >
                        Learn More
                      </a>
                    </CardContent>
                  </Card>
                </div>
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
