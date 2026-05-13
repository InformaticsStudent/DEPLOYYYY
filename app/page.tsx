import React from 'react';

export default function Portfolio() {
  return (
    <div className="bg-[#0f172a] min-h-screen text-slate-200 selection:bg-cyan-500/30 font-sans">
      {/* Navbar */}
      <nav className="fixed top-0 w-full z-50 bg-[#0f172a]/80 backdrop-blur-md border-b border-slate-800">
        <div className="max-w-5xl mx-auto px-6 h-16 flex items-center justify-between">
          <span className="text-cyan-400 font-bold text-xl tracking-tighter">Riki Efendi</span>
          <div className="hidden md:flex space-x-8 text-sm font-medium">
            <a href="#about" className="hover:text-cyan-400 transition">About</a>
            <a href="#projects" className="hover:text-cyan-400 transition">Projects</a>
            <a href="mailto:riki38187@gmail.com" className="bg-cyan-500 text-slate-900 px-4 py-2 rounded-full hover:bg-cyan-400 transition">Contact</a>
          </div>
        </div>
      </nav>

      <main className="max-w-5xl mx-auto px-6 pt-32">
        {/* Hero Section */}
        <section id="about" className="py-20">
          {/* BAGIAN GAMBAR PROFIL */}
          <div className="mb-8 relative group w-32 h-32">
            <div className="absolute inset-0 bg-cyan-500 rounded-2xl rotate-6 group-hover:rotate-0 transition-transform duration-300"></div>
            <img 
              src="/efendi.jpg.jpeg" 
              alt="profile 1" 
              className="relative z-10 w-32 h-32 rounded-2xl bg-slate-800 object-cover border-2 border-slate-700"
            />
          </div>
          <h2 className="text-cyan-400 font-mono mb-4 text-lg">Welcome to my Portofolio</h2>
          <h1 className="text-5xl md:text-7xl font-bold text-slate-100 mb-6">
            M. Riki Efendi.
          </h1>
          <h3 className="text-4xl md:text-6xl font-bold text-slate-400 mb-8">
            I prioritize appearance.
          </h3>
          <p className="max-w-xl text-slate-400 text-lg leading-relaxed mb-10">
            Salken guys, aku riki efendi biasa di panggil ependi, ini project coba" pertama ku yak. 
            Skrg, aku lagi mendalami bahasa pemrograman <span className="text-cyan-400">Next.js</span> dan <span className="text-cyan-400">Tailwind CSS</span>.
          </p>
          <div className="flex gap-4">
            <button className="border border-cyan-500 text-cyan-500 px-6 py-3 rounded-lg hover:bg-cyan-500/10 transition">
              Cek Portofolio
            </button>
          </div>
        </section>

        {/* Project Section */}
        <section id="projects" className="py-20">
          <h2 className="text-2xl font-bold mb-10 flex items-center">
            <span className="text-cyan-400 font-mono mr-2 text-xl">01.</span> My Projects
          </h2>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div className="group bg-slate-800/40 p-8 rounded-2xl border border-slate-700 hover:border-cyan-500/50 transition-all hover:-translate-y-2">
              <h3 className="text-xl font-bold mb-2 group-hover:text-cyan-400">Web Portofolio</h3>
              <p className="text-slate-400 text-sm mb-4 leading-relaxed">Website portofolio tema gelap, yang aku bangun pake Next.js.</p>
              <div className="flex gap-3 text-xs font-mono text-cyan-400/80">
                <span>Next.js</span> <span>Tailwind</span> <span>Vercel</span>
              </div>
            </div>
            
            <div className="group bg-slate-800/40 p-8 rounded-2xl border border-slate-700 hover:border-cyan-500/50 transition-all hover:-translate-y-2">
              <h3 className="text-xl font-bold mb-2 group-hover:text-cyan-400">Project Terbaru</h3>
              <p className="text-slate-400 text-sm mb-4 leading-relaxed">Project sedang dalam pengembangan.</p>
              <div className="flex gap-3 text-xs font-mono text-cyan-400/80">
                <span>React</span> <span>TypeScript</span> <span>API</span>
              </div>
            </div>
          </div>
        </section>
      </main>

      <footer className="text-center py-10 border-t border-slate-800 mt-20">
        <p className="text-slate-500 text-sm font-mono tracking-widest">
          © 2026 M. RIKI EFENDI
        </p>
      </footer>
    </div>
  );
}