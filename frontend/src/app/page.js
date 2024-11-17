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
import { Input } from '@/components/ui/input';
import { Label } from '@/components/ui/label';
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from '@/components/ui/select';

export function CardWithForm({ className, ...props }) {
  return (
    <div
      style={{
        position: 'relative',
        justifyContent: 'flex-end',
        height: '100vh',
      }}
    >
      <Card
        className={cn(className)}
        {...props}
        style={{
          position: 'fixed',
          top: '50%',
          left: '76.66%',
          transform: 'translate(-50%, -50%)',
          width: '400px',
          height: '300px',
          backgroundColor: '#1F2937',
          border: '2px solid rgba(255,255,255,0.2)',
          borderRadius: '12px',
          boxShadow: '0 4px 8px rgba(0,0,0,0.2)',
          color: 'white',
        }}
      >
        <CardHeader
          style={{
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'center',
          }}
        >
          <CardTitle>Welcome!</CardTitle>
          <CardDescription></CardDescription>
        </CardHeader>
        <CardContent>
          <p>
            This is a great website to learn more about all the possibilities of
            NASA events and internship opportunities
          </p>
        </CardContent>
        <CardFooter
          style={{
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'center',
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
