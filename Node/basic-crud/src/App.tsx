import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import Login from "./pages/auth/Login";
import SignUp from "./pages/auth/SignUp";
import Dashboard from "./pages/Dashboard";
import Home from "./pages/dashbContent/Home";
import Entry from "./pages/dashbContent/Entry";

function App() {
  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Navigate to="/login" replace />} />
          <Route path="/login" element={<Login />} />
          <Route path="/signup" element={<SignUp />} />

          <Route path="/dashboard" element={<Dashboard />}>
            <Route index element={<Home />} />
            <Route path="entry" element={<Entry />} />
          </Route>
        </Routes>
      </BrowserRouter>
    </>
  )
}

export default App