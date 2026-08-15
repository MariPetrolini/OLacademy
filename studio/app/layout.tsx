import type {Metadata} from 'next';import './globals.css';
export const metadata:Metadata={title:'OL Academy · Estúdio de Aulas',description:'Produção guiada de cursos profissionais, do roteiro ao vídeo final.'};
export default function RootLayout({children}:{children:React.ReactNode}){return <html lang="pt-BR"><body>{children}</body></html>}
