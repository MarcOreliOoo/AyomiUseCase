import { ThemeProvider } from "@/components/theme-provider";
import Calculator from "./components/Calculator";
import Header from "./components/header/Header";

function App() {
    return (
        <ThemeProvider defaultTheme="dark" storageKey="vite-ui-theme">
            <Header />
            <div className="section-min-height flex h-full flex-row items-center justify-center bg-slate-400">
                <Calculator />
            </div>
        </ThemeProvider>
    );
}

export default App;
