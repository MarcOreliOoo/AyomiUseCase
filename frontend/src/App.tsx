import { ThemeProvider } from "@/components/theme-provider";
import CalculatorContainer from "./components/calculator/CalculatorContainer";
import Header from "./components/header/Header";

function App() {
    return (
        <ThemeProvider defaultTheme="dark" storageKey="vite-ui-theme">
            <Header />
            <div className="section-min-height flex h-full flex-row items-center justify-center bg-primary/90">
                <CalculatorContainer />
            </div>
        </ThemeProvider>
    );
}

export default App;
