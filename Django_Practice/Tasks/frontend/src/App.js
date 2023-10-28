import React, { useState, useEffect } from "react";
import axios from "axios";

function App() {
  const [details, setDetails] = useState([]);
  const [update, setUpdate] = useState([]);
  const [singleData, setSingleData] = useState([]);
  const divStyle = {
    color: "red",
    backgroundColor: "lightgray",
    fontSize: "20px",
    padding: "10px",
    margin: "7px",
    boxShadow:
      " rgba(0, 0, 0, 0.4) 0px 2px 4px, rgba(0, 0, 0, 0.3) 0px 7px 13px -3px, rgba(0, 0, 0, 0.2) 0px -3px 0px inset",
  };
  const card={
    width:'18rem',
  }

  // Get all user

  let apiUrl = "http://127.0.0.1:8000/";
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get(apiUrl);
        setDetails(response.data);
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };

    fetchData();
  }, []);


  const fetchData1 = async (id) => {
    try {
      const response = await axios.get(`http://127.0.0.1:8000/app/${id}`,{
        // data: { id }, 
        headers: {
          'Content-Type': 'application/json',
        }
      });
      console.log(response.data)
      setSingleData(response.data);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  useEffect((id) => {
    fetchData1(id);

  }, []);

  const handleButtonClick = (id) => {
    console.log(id)
    fetchData1(id);
  };



  // Data sending
  const [formData, setFormData] = useState({
    employee: '',
    department: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async(e) => {
    // e.preventDefault();
    await axios
      .post(apiUrl,JSON.stringify(formData), {
        headers: {
          'Content-Type': 'application/json',
        }
      })
      .then((response) => {
        console.log('Data sent successfully:', response.data);
      })
      .catch((error) => {
        console.log('Error sending data:', error);
      });
  };

  // Delete
  const handleDelete = async (id) => {
    try {
      const response = await axios.delete(apiUrl,{
        data: { id }, 
        headers: {
          'Content-Type': 'application/json',
        }
      });
      console.log('Item deleted:', response.data);
    } catch (error) {
      console.error('Error deleting item:', error);
    }
  }
  return (
    <div>
      <p style={divStyle}> Data Stored in Django Rest Framework & Rendered and Generated in React</p>
    
    <div className="container">
      <div className="row">
          {details.map((item, id) => (
          <div className="card my-4 col-sm-12 col-md-6 col-lg-4 mx-3" style={card}>
              <div className="card-body ">
                  <div className="d-flex ">
                      <h5 className="card-title d-inline flex-grow-1 "title="Title">{item.employee}</h5>
                      <div className="px-2"title="Update"><svg xmlns="http://www.w3.org/2000/svg" width="18"       height="18" fill="currentColor" className="bi bi-pencil-square" onClick={()=>handleButtonClick(item.ID)} viewBox="0  0 16 16">
                          <path d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"/>
                          <path fill-rule="evenodd" d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z"/>
                        </svg></div>
                      <button type="button" title="Delete" className="btn-close d-inline "onClick={() => handleDelete(item.ID)} aria-label="Close"></button>
                  </div>
                <hr />
                <p className="card-text"title="Description">{item.department}</p>
      
              </div>
          </div>
          ))}
      </div>
      {/* form for data send */}
<div className="mx-5">
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="employee"
          className="my-3"
          value={setUpdate.employee}
          onChange={handleChange}
          placeholder="Title"
        /> <br />
        <textarea
          type="textarea"
          name="department"
          className="my-3"
          value={setUpdate.department}
          onChange={handleChange}
          placeholder="Description"
         rows="4" cols="50">

        </textarea>
        
        <br />
        <button type="submit" className="mb-5 btn btn-outline-primary">Submit Data</button>
      </form>
      </div>
    </div>

    </div>
  );
}

export default App;
