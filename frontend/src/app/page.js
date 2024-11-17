'use client';

import * as React from 'react';

import Link from 'next/link';
import { Button } from '@/components/ui/button';
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from '@/components/ui/card';
import { cn } from '@/lib/utils';

export function CardWithForm({ className, ...props }) {
  return (
    <div
      style={{
        position: 'relative',
        display: 'flex',
        justifyContent: 'flex-end', // Align card to the right
        alignItems: 'center', // Center vertically
        height: '100vh', // Full page height
        paddingRight: '5%', // Add padding to the right side
      }}
    >
      <Card
        className={cn(className)}
        {...props}
        style={{
          position: 'relative',
          width: '90%',
          maxWidth: '400px', // Max width for the card
          backgroundColor: '#1F2937', // Transparent white background
          border: '2px solid rgba(255,255,255,0.2)',
          borderRadius: '12px',
          boxShadow: '0 4px 8px rgba(0,0,0,0.2)',
          color: 'white',
          padding: '1rem',
          overflow: 'hidden',
        }}
      >
        <CardHeader
          style={{
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            marginBottom: '1rem',
          }}
        >
          <CardTitle className='text-xxl font-bold'>Welcome!</CardTitle>
        </CardHeader>
        <CardContent>
          <p className='text-med leading-relaxed text-center'>
            Welcome to your gateway to endless possibilities at NASA! Here, you
            can uncover opportunities that align with your passions, field of
            study, and major, empowering you to launch an inspiring career in
            space exploration, innovation, and discovery. Whether you're driven
            by engineering, science, or creative problem-solving, this platform
            connects you to internships, research projects, and events tailored
            to your dreams. Together, let's turn your aspirations into reality
            and ignite a future where you reach for the stars.
          </p>
        </CardContent>
        <CardFooter
          style={{
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'center',
            marginTop: '1rem',
            color: 'black',
          }}
        >
          <Link href='/launch'>
            <Button variant='outline'>Launch</Button>
          </Link>
        </CardFooter>
      </Card>
    </div>
  );
}

export default CardWithForm;
