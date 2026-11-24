/**
 * The fonts available to your theme (src/theme.ts picks the pairing).
 * All are loaded self-hosted by Next.js: no layout shift, no CDN calls.
 */
import { Fraunces, Inter, Lora, Space_Grotesk, Cormorant_Garamond} from "next/font/google";

export const inter = Inter({ subsets: ["latin"], variable: "--font-inter" });
export const fraunces = Fraunces({ subsets: ["latin"], variable: "--font-fraunces" });
export const spaceGrotesk = Space_Grotesk({ subsets: ["latin"], variable: "--font-space-grotesk" });
export const lora = Lora({ subsets: ["latin"], variable: "--font-lora" });
export const cormorantGaramond = Cormorant_Garamond({ subsets: ["latin"], variable: "--font-cormorant-garamond" });

export const fontVariables = [
  inter.variable,
  fraunces.variable,
  spaceGrotesk.variable,
  lora.variable,
  cormorantGaramond.variable,
].join(" ");
