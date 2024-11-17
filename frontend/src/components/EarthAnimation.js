'use client';

import React, { useEffect, useRef } from 'react';
import * as THREE from 'three';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls';

const EarthAnimation = () => {
  const mountRef = useRef(null);

  useEffect(() => {
    let camera, scene, renderer, globe, controls, clock;

    const init = () => {
      clock = new THREE.Clock();

      // Camera
      camera = new THREE.PerspectiveCamera(
        25,
        window.innerWidth / window.innerHeight,
        0.1,
        100
      );
      camera.position.set(4.5, 2, 3);

      // Scene
      scene = new THREE.Scene();

      // Sun
      const sun = new THREE.DirectionalLight('#ffffff', 2);
      sun.position.set(0, 0, 3);
      scene.add(sun);

      // Texture Loader
      const textureLoader = new THREE.TextureLoader();
      const dayTexture = textureLoader.load('/textures/earth_day_4096.jpg');
      const bumpTexture = textureLoader.load(
        '/textures/earth_bump_roughness_clouds_4096.jpg'
      );

      // Globe Material
      const globeMaterial = new THREE.MeshStandardMaterial({
        map: dayTexture,
        bumpMap: bumpTexture,
        roughness: 0.5,
      });

      // Globe Geometry
      const sphereGeometry = new THREE.SphereGeometry(1, 64, 64);
      globe = new THREE.Mesh(sphereGeometry, globeMaterial);
      scene.add(globe);

      // Renderer
      renderer = new THREE.WebGLRenderer({ antialias: true });
      renderer.setSize(window.innerWidth, window.innerHeight);
      renderer.setPixelRatio(window.devicePixelRatio);

      if (mountRef.current) {
        mountRef.current.appendChild(renderer.domElement);

        // Prevent scroll wheel zoom directly
        mountRef.current.addEventListener('wheel', (event) => {
          event.preventDefault();
        });
      }

      // Controls
      controls = new OrbitControls(camera, renderer.domElement);
      controls.enableDamping = true; // Smooth camera movement
      controls.enableZoom = false; // Explicitly disable zoom
      controls.zoomSpeed = 0; // Ensure zoom speed is zero

      // Resize Event
      window.addEventListener('resize', onWindowResize);

      animate();
    };

    const onWindowResize = () => {
      camera.aspect = window.innerWidth / window.innerHeight;
      camera.updateProjectionMatrix();
      renderer.setSize(window.innerWidth, window.innerHeight);
    };

    const animate = () => {
      requestAnimationFrame(animate);
      const delta = clock.getDelta();
      globe.rotation.y += delta * 0.1;
      controls.update();
      renderer.render(scene, camera);
    };

    init();

    // Cleanup
    return () => {
      if (mountRef.current) {
        mountRef.current.innerHTML = ''; // Safely clear content
        mountRef.current.removeEventListener('wheel', (event) =>
          event.preventDefault()
        ); // Remove wheel listener
      }
      if (renderer) {
        renderer.dispose(); // Dispose of renderer
      }
      window.removeEventListener('resize', onWindowResize);
    };
  }, []);

  return <div ref={mountRef} style={{ width: '100%', height: '100vh' }} />;
};

export default EarthAnimation;
