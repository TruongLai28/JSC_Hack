"use client";

import React, { useEffect, useRef } from "react";
import * as THREE from "three";
import { OrbitControls } from "three/examples/jsm/controls/OrbitControls";

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
      const sun = new THREE.DirectionalLight("#ffffff", 2);
      sun.position.set(0, 0, 3);
      scene.add(sun);

      // Texture Loader
      const textureLoader = new THREE.TextureLoader();
      const dayTexture = textureLoader.load("/textures/earth_day_4096.jpg");
      const nightTexture = textureLoader.load("/textures/earth_night_4096.jpg");
      const bumpTexture = textureLoader.load(
        "/textures/earth_bump_roughness_clouds_4096.jpg"
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
      mountRef.current.appendChild(renderer.domElement);

      // Controls
      controls = new OrbitControls(camera, renderer.domElement);
      controls.enableDamping = true;

      // Resize Event
      window.addEventListener("resize", onWindowResize);

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
      mountRef.current.innerHTML = "";
      renderer.dispose();
    };
  }, []);

  return <div ref={mountRef} style={{ width: "100%", height: "100vh" }} />;
};

export default EarthAnimation;
