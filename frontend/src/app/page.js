'use client';

import * as React from 'react';

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
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        height: '100vh',
        backgroundColor: '#f0f0f0',
      }}
    >
      <Card
        className={cn('w-[380px]', className)}
        {...props}
        style={{
          backgroundColor: 'transparent',
          border: '1px solid rgba(255,255,255,0.2)',
          borderRadius: '12px',
          padding: '16px',
          boxShadow: '0 4px 8px rgba(0,0,0,0.2)',
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
          }}
        >
          <Button variant='outline'>Launch</Button>
        </CardFooter>
      </Card>
    </div>
  );
}

export default CardWithForm;
