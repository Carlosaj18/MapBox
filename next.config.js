/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
};

module.exports = {
  images: {
    // domains: ['upload.wikimedia.org']
    domains: [
      "links.papareact.com",
      "jsonkeeper.com",
      "api.npoint.io",
      "www.nauticareport.it",
      "a0.muscache.com",
      "images.fineartamerica.com",
      "i.ebayimg.com",
      "www.thetimes.co.uk",
    ],
  },
  nextConfig,
  env: {
    MAPBOX_KEY: process.env.NEXT_PUBLIC_MAPBOX_KEY,
  },
};
