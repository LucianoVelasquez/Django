"use client";
import axios from "axios";
import { useState } from "react";

function Form() {
  const [newTask, setTaks] = useState({});
  const postTasks = async (e) => {
    try {
      e.preventDefault();
      await axios.post("http://localhost:3001/tasks/api/v1/tasks/",newTask);
      console.log("Se envio la info");
      return;
    } catch (error) {
      console.log(error);
    }
  };
  const handlerChange = (e) => {
    const type = e.target.name;
    const value = e.target.value;

    if (type === "description") {
      setTaks({ ...newTask, description: value });
    } else {
      setTaks({ ...newTask, title: value });
    }
  };
  return (
    <div className="flex flex-col items-center mt-5">
      <h1 className="text-5xl">Form</h1>

      <h2 className="text-3xl mt-8">POST TASK</h2>

      <div className="mt-4 bg-slate-800 h-auto w-80 p-4 rounded-lg">
        <form
          onSubmit={(e) => {
            postTasks(e);
          }}
          className="flex flex-col"
        >
          <div className="flex justify-center items-center">
            <label className="mr-2">Title:</label>
            <input
              onChange={(e) => {
                handlerChange(e);
              }}
              className="mt-4 mb-4 text-stone-900"
              type="text"
              name="title"
            ></input>
          </div>
          <div className="flex justify-center items-center">
            <label className="mr-2">Description:</label>
            <textarea
              onChange={(e) => {
                handlerChange(e);
              }}
              className="mt-4 mb-4 text-stone-900"
              name="description"
            ></textarea>
          </div>
          <input
            type="submit"
            className="bg-slate-950 rounded-xl hover:bg-slate-900 "
          ></input>
        </form>
      </div>
    </div>
  );
}

export default Form;
