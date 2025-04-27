import { useState, useRef } from 'react'
import './App.css'

export default function BotanicalensApp() {
  const [file, setFile] = useState(null);
  const [isDragging, setIsDragging] = useState(false);
  const [isSubmitted, setIsSubmitted] = useState(false);
  const [preview, setPreview] = useState(null);
  const [error, setError] = useState(null);
  const fileInputRef = useRef(null);

  const handleFileChange = (selectedFile) => {
    const validExtensions = ["image/jpeg", "image/jpg", "image/png"];
    
    if (selectedFile && validExtensions.includes(selectedFile.type)) {
      setFile(selectedFile);
      setError(null);
      
      const reader = new FileReader();
      reader.onload = () => {
        setPreview(reader.result);
      };
      reader.readAsDataURL(selectedFile);
    } else if (selectedFile) {
      setError('Invalid file type. Please upload a JPEG, JPG or PNG image.');
      setFile(null);
      setPreview(null);
    }
  };

  const handleInputChange = (e) => {
    handleFileChange(e.target.files[0]);
  };

  const handleDragOver = (e) => {
    e.preventDefault();
    setIsDragging(true);
  };

  const handleDragLeave = () => {
    setIsDragging(false);
  };

  const handleDrop = (e) => {
    e.preventDefault();
    setIsDragging(false);
    handleFileChange(e.dataTransfer.files[0]);
  };

  const handleBrowseClick = () => {
    fileInputRef.current.click();
  };

  const handleSubmit = () => {
    if (file) {
      setIsSubmitted(true);
      // Here you would typically handle the actual submission to a backend
      console.log("File submitted:", file);
    } else {
      setError('Please select a file first.');
    }
  };

  const handleReset = () => {
    setFile(null);
    setPreview(null);
    setIsSubmitted(false);
    setError(null);
  };

  return (
    <div className="w-full h-screen overflow-y-hidden overflow-x-hidden flex flex-col bg-green-950 bg-cover bg-center bg-no-repeat">
      {/* Navbar */}
      <nav className="w-full bg-green-900 p-4 flex justify-between items-center">
        <div className="text-white font-bold text-xl md:text-2xl flex items-center">
          <span className="underline font-serif">Botanicalens</span>
          <i className="fa-solid fa-magnifying-glass fa-flip-horizontal ml-2" style={{ color: "#ffffff" }}></i>
        </div>
        <div className="flex gap-4">
          <a href="#" className="text-white hover:text-green-200">Home</a>
          <a href="#" className="text-white hover:text-green-200">Resources</a>
          <a href="#" className="text-white hover:text-green-200">About</a>
        </div>
      </nav>

      {/* Main Content */}
      <div className="flex-1 flex flex-col items-center justify-center w-full px-4 py-8">
        <h1 className="text-4xl md:text-6xl lg:text-8xl font-bold text-white mb-8 font-serif text-center">
          <u>Botanicalens</u>
          <i className="fa-solid fa-magnifying-glass fa-flip-horizontal ml-2" style={{ color: "#ffffff" }}></i>
        </h1>

        {isSubmitted ? (
          <div className="bg-white p-8 rounded-lg text-center w-full max-w-md">
            <div className="text-green-700 mb-4">
              <i className="fa-solid fa-circle-check text-5xl"></i>
            </div>
            <h2 className="text-2xl font-bold text-green-700 mb-4">File Submitted Successfully!</h2>
            <p className="mb-6 text-gray-700">Your image has been processed.</p>
            <button 
              onClick={handleReset}
              className="bg-green-700 text-white px-6 py-2 rounded-md hover:bg-green-800 transition duration-300"
            >
              Upload Another
            </button>
          </div>
        ) : (
          <>
            <div 
              className={`border-2 ${isDragging ? 'border-solid' : 'border-dashed'} border-white rounded-lg w-full max-w-4xl mx-auto aspect-video flex flex-col items-center justify-center ${preview ? 'p-0 overflow-hidden' : 'p-8'}`}
              onDragOver={handleDragOver}
              onDragLeave={handleDragLeave}
              onDrop={handleDrop}
            >
              {preview ? (
                <img src={preview} alt="Preview" className="w-full h-full object-cover rounded-lg" />
              ) : (
                <>
                  <i className="fa-solid fa-cloud-arrow-up text-white text-4xl md:text-6xl mb-4"></i>
                  <h2 className="text-xl md:text-2xl font-medium text-white mb-2 text-center">
                    {isDragging ? 'Release to Upload File' : 'Drag & Drop to Upload File'}
                  </h2>
                  <p className="text-lg md:text-xl text-white mb-4">OR</p>
                  <button 
                    onClick={handleBrowseClick}
                    className="bg-white text-green-700 px-6 py-2 rounded-md hover:bg-gray-100 transition duration-300"
                  >
                    Browse File
                  </button>
                  <input 
                    type="file" 
                    ref={fileInputRef}
                    className="hidden" 
                    onChange={handleInputChange}
                    accept=".jpg,.jpeg,.png"
                  />
                </>
              )}
            </div>

            {error && (
              <div className="mt-4 text-red-400 text-center">
                <p>{error}</p>
              </div>
            )}

            <div className="mt-6 flex justify-center">
              <button 
                onClick={handleSubmit}
                className={`px-6 py-2 rounded-md transition duration-300 ${file ? 'bg-white text-green-700 hover:bg-gray-100' : 'bg-gray-400 text-gray-700 cursor-not-allowed'}`}
                disabled={!file}
              >
                Submit
              </button>
              {file && (
                <button
                  onClick={handleReset}
                  className="ml-4 px-6 py-2 bg-red-500 text-white rounded-md hover:bg-red-600 transition duration-300"
                >
                  Cancel
                </button>
              )}
            </div>
          </>
        )}
      </div>

      {/* Footer */}
      <footer className="w-full bg-green-900 p-4 text-center text-white mt-auto">
        <p>© 2025 Botanicalens. All rights reserved.</p>
      </footer>
    </div>
  );
}
